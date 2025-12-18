---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerDnsSecPublicKey_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/export-dnsserverdnssecpublickey?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-DnsServerDnsSecPublicKey
---

# Export-DnsServerDnsSecPublicKey

## 摘要
导出DNSSEC签名区域的DS和DNSKEY信息。

## 语法

### DnsKey（默认值）
```
Export-DnsServerDnsSecPublicKey [-ComputerName <String>] [-ZoneName] <String> [-Path <String>] [-PassThru]
 [-UnAuthenticated] [-Force] [-NoClobber] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### DS
```
Export-DnsServerDnsSecPublicKey [-ComputerName <String>] [-ZoneName] <String> [-Path <String>] [-PassThru]
 [-UnAuthenticated] [-Force] [-NoClobber] -DigestType <String[]> [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-DnsServerDnsSecPublicKey` cmdlet 用于导出已使用域名系统安全扩展（DNSSEC）签名的区域的委托签名者（DS，即负责生成签名数据的实体）或域名系统公钥（DNSKEY）信息。

## 示例

### 示例 1：将信任锚导出到文件共享位置
```
PS C:\> Export-DnsServerDnsSecPublicKey -ComputerName "DNSDC1.Contoso.com" -ZoneName "Contoso.com" -Path "\\MyDNSKeyShare\keys" -PassThru -DigestType "Sha1"

Exporting a trust anchor without using authentication is insecure unless DNSSEC is active on "${ComputerName}", a trust anchor covering "${ZoneName}" is installed, and the connection between the local machine and "${ComputerName}" is secure. Consider alternative means of exporting the trust anchors, such as the DNSCMD protocol, email, or HTTPS. Proceed? [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```

此命令将 Contoso.com 的信任锚点（DS 记录）导出到文件共享中。DNS 管理员从托管 Contoso.com 区域的 DNS 服务器上运行该命令，并指定区域签名密钥使用 SHA-1 算法来创建 DS 记录。

此命令会在 `\\\\MyDNSKeyShare\keys` 目录下创建一个名为 Dsset-Contoso.com 的文件，并以 `Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DNS/DnsServerResourceRecord` 的格式写入相应的 DNS 记录。

### 示例 2：利用未经授权的访问权限导出信任锚点
```
PS C:\> Export-DnsServerDnsSecPublicKey -ComputerName "DNSDC1.contoso.com" -ZoneName "Contoso.com" - Path "\\MyDNSKeyShare\keys" -PassThru -UnAuthorized -Force

Exporting a trust anchor without using authentication is insecure unless DNSSEC is active on "${ComputerName}", a trust anchor covering "${ZoneName}" is installed, and the connection between the local machine and "${ComputerName}" is secure. Consider alternative means of exporting the trust anchors, such as the DNSCMD protocol, email, or HTTPS. Proceed? [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
Note: User typing N exits out of the command with no export or output
```

此命令将 Contoso.com 的信任锚点（DNSKEY 记录）导出到一个文件共享位置。执行该命令的 DNS 管理员没有对托管 Contoso.com 区域的 DNS 服务器的访问权限。该命令指定区域签名密钥使用 SHA-1 算法来生成 DS 记录。

该命令在 `\\\\MyDNSKeyShare\keys` 目录下创建一个名为 Keyset-Contoso.com 的文件，并以 `Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DNS/DnsServerResourceRecord` 的格式写入相应的 DNS 记录。

### 示例 3：获取所有已签名区域的信任锚点
```
PS C:\> Get-DnsServerZone | ForEach-Object {Export-DnsServerDnsSecPublicKey -ComputerName "DNSDC1.Contoso.com" -ZoneName "Contoso.com" -Path "\\MyDNSKeyShare\keys" -PassThru -UnAuthorized -Force  }
```

这个命令用于获取托管在DNS服务器Contoso.com上的所有已签名区域的信任锚点。在这种情况下，该DNS服务器当前正在为contoso.com、dinnernow.com和hrweb.net这三个域名提供已签名的区域服务。

该命令使用 `ForEach-Object` cmdlet 来导出信任锚点，并通过管道运算符（pipeline operator）将结果传递给 `Get-DnsServerZone` cmdlet。

此命令会在共享文件夹中为每个托管在DNS服务器上的已签名区域创建一个密钥集文件（Keyset-Contoso.com、Keyset-Dinnernow.com、Keyset-Hrweb.net），并将DNSKEY记录以Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DNS/DNS/DnsServerResourceRecord的格式写入相应的文件中。

### 示例 4：将信任锚导入到未经授权的域名服务器（DN server）
```
PS C:\> $publicKey = Export-DnsServerDnssecPublicKey -ZoneName "contoso.com" -Path "C:\" -PassThru -UnAuthenticated -Force
PS C:\> $publicKey[0].RecordData | Add-DnsServerTrustAnchor -Name "constoso.com" -ComputerName "DNSDC1.Contoso.com"
```

第一个命令将 Contoso.com 的信任锚点（DNSKEY 记录）导出到指定的路径，并将结果存储在 `$publicKey` 变量中。参数 `Unauthenticated` 表示执行此命令的 DNS 管理员没有权限访问托管 Contoso.com 区域的 DNS 服务器。

第二个命令将从 Contoso.com 导出的第一个信任记录添加到一个名为 DNSDC1 的非权威 DNS 服务器中。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job` cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全限定域名（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -DigestType
指定一个算法数组，该区域签名密钥使用这些算法来创建DNS记录。此参数的可接受值包括：  
- Sha1  
- Sha256  
- Sha384

```yaml
Type: String[]
Parameter Sets: DS
Aliases:
Accepted values: Sha1, Sha256, Sha384

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Force
在未要求您确认的情况下直接导出签名密钥。默认情况下，该cmdlet在执行前会先提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoClobber
指定导出操作不会覆盖同名의现有导出文件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定该 cmdlet 用于存放密钥集文件的绝对路径。cmdlet 会根据区域名称自动为文件命名。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略了此参数或输入了 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的限制值。这个限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UnAuthenticated
这表示当前执行此 cmdlet 的用户尚未经过身份验证。无论您是否具有在远程 DNS 服务器上运行该 cmdlet 的权限，提供者（DNS 服务器）都会查询 DS 或 DNSKEY 相关信息，并导出所需的数据。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -ZoneName
指定主要区域的名称，该命令行脚本（cmdlet）会将签名密钥导出到此区域。

```yaml
Type: String
Parameter Sets: (All)
Aliases: TrustPointName, TrustAnchorName

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerResourceRecord

## 备注

## 相关链接

[Add-DnsServerTrustAnchor](./Add-DnsServerTrustAnchor.md)

[Get-DnsServerZone](./Get-DnsServerZone.md)

