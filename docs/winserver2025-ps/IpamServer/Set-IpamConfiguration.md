---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamConfiguration.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/set-ipamconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IpamConfiguration
---

# 设置 IPAM 配置

## 摘要
修改运行 IPAM 服务器的计算机的配置。

## 语法

### SetIpamConfiguration0
```
Set-IpamConfiguration [-Port] <UInt16> [-Force] [-PassThru] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SetIpamConfiguration4
```
Set-IpamConfiguration [-Force] [-PassThru] [-UpdateTables] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SetIpamConfiguration3
```
Set-IpamConfiguration [-Force] [-PassThru] -HmacKey <SecureString> [-UpdateTables] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SetIpamConfiguration2
```
Set-IpamConfiguration [-Force] [-PassThru] [-RefreshHmacKey] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SetIpamConfiguration1
```
Set-IpamConfiguration [-Force] [-PassThru] [-ProvisioningMethod] <ProvisioningMethod> [[-GpoPrefix] <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-IpamConfiguration` cmdlet 用于修改 IP 地址管理（IPAM）服务器的配置，包括运行 IPAM 远程服务器管理工具（RSAT）客户端的主机与运行 IPAM 服务器的主机之间进行连接和通信所使用的 TCP 端口。

## 示例

#### 示例 1：修改 IPAM 配置
```
PS C:\> Set-IpamServerConfiguration -Port 45000  -PassThru -Force
Version : 1.3

 Port : 45000
```

这个命令将 IPAM 服务器的管理端口更改为 45000，并屏蔽默认的确认提示信息。此外，该命令还会返回修改后的 IPAM 服务器配置对象。

该命令包含了 *PassThru* 参数，因此它会将结果显示在控制台上。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业的结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm
在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Force
强制命令运行，而无需请求用户确认。

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

### -GpoPrefix
指定 IPAM 用于创建组策略对象的唯一组策略对象（GPO）前缀名称。仅当 *ProvisioningMethod* 参数的值设置为 “Automatic” 时，才使用此参数。

```yaml
Type: String
Parameter Sets: SetIpamConfiguration1
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HmacKey
指定一个基于密钥散列的消息认证码（HMAC）。

```yaml
Type: SecureString
Parameter Sets: SetIpamConfiguration3
Aliases:

Required: True
Position: Named
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

### -Port
指定用于运行 IPAM RSAT 客户端的计算机与 IPAM 服务器之间通信的 TCP 端口号。IPAM 允许您在 1-65535 的范围内配置任意端口号，以实现客户端与服务器之间的通信。为了避免与已知端口发生冲突，请从未分配的端口号范围（48620-49150）中选择一个端口。默认情况下，IPAM 使用端口号 48885。该 cmdlet 会为指定的新端口配置相应的自定义 IPAM 服务器防火墙规则，并重新启动 IPAM 应用程序池以使其监听该新端口。

```yaml
Type: UInt16
Parameter Sets: SetIpamConfiguration0
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ProvisioningMethod
指定一种配置（provisioning）方法。

该参数的可接受值为：Automatic（自动）和Manual（手动）。

```yaml
Type: ProvisioningMethod
Parameter Sets: SetIpamConfiguration1
Aliases:
Accepted values: Automatic, Manual

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RefreshHmacKey
表示如果HMAC密钥已过期，该cmdlet会刷新该密钥。

```yaml
Type: SwitchParameter
Parameter Sets: SetIpamConfiguration2
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -UpdateTables
表示该cmdlet会更新数据库表中的数据。

```yaml
Type: SwitchParameter
Parameter Sets: SetIpamConfiguration4
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: SwitchParameter
Parameter Sets: SetIpamConfiguration3
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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Windows.Ipam Commands.IpamConfiguration
此cmdlet返回一个包含IPAM配置的对象。

## 备注

## 相关链接

[Get-IpamConfiguration](./Get-IpamConfiguration.md)

