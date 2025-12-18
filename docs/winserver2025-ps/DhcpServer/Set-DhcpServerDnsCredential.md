---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerDnsCredential_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/set-dhcpserverdnscredential?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DhcpServerDnsCredential
---

# 设置 DHCP 服务器的 DNS 凭据

## 摘要
设置 DHCP 服务器服务用于在 DNS 服务器上注册或注销客户端记录的凭据。

## 语法

```
Set-DhcpServerDnsCredential [-ComputerName <String>] [-Credential] <PSCredential> [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DhcpServerDnsCredential` cmdlet 用于设置动态主机配置协议（DHCP）服务器服务在域名系统（DNS）服务器上注册或注销客户端记录时所使用的凭据。

## 示例

### 示例 1：为 DHCP 服务器设置凭据
```
PS C:\> $Credential = Get-Credential
PS C:\> Set-DhcpServerDnsCredential -Credential $Credential -ComputerName "DhcpServer03.Contoso.com"
```

这个示例将凭据保存在DHCP服务器上。DHCP服务器使用该凭据在DNS服务器上注册或注销客户端记录。

第一个命令使用 **Get-Credential** cmdlet 来创建一个 **PSCredential** 对象，然后将其存储在 `$Credential` 变量中。该 cmdlet 会提示您输入用户名和密码。有关更多信息，请输入 `Get-Help Get-Credential`。

第二个命令指定了存储在 `$Credential` 变量中的凭据对象，该凭据用于名为 `DhcpServer03.Contoso.com` 的 DHCP 服务器。

### 示例 2：提示用户输入 DHCP 服务器的凭据
```
PS C:\> Set-DhcpServerDnsCredential -ComputerName "DhcpServer03.Contoso.com"
```

此命令用于设置运行DHCP服务器的机器在向DNS服务器注册和注销客户端记录时所使用的DNS凭据。该cmdlet会提示您输入用户名和密码。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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
指定运行DHCP服务器服务的目标计算机的DNS名称或IP地址。

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
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Credential
指定一个基于用户名和密码的 **PSCredential** 对象。要获取一个 **PSCredential** 对象，请使用 **Get-Credential** cmdlet。有关更多信息，键入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DhcpServerDnsCredential

## 备注

## 相关链接

[Get-DhcpServerDnsCredential](./Get-DhcpServerDnsCredential.md)

[Remove-DhcpServerDnsCredential](./Remove-DhcpServerDnsCredential.md)

