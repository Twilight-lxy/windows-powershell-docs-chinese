---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterIPsecOffload.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/set-netadapteripsecoffload?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-NetAdapterIPsecOffload
---

# 将 NetAdapter 的 IPsec Offload 功能设置为关闭状态

## 摘要
设置网络适配器的 IPsec 负载卸载属性。

## 语法

### 按名称查找（默认方式）
```
Set-NetAdapterIPsecOffload [-Name] <String[]> [-IncludeHidden] [-Enabled <Boolean>] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByInstanceID
```
Set-NetAdapterIPsecOffload -InterfaceDescription <String[]> [-IncludeHidden] [-Enabled <Boolean>] [-NoRestart]
 [-PassThru] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-NetAdapterIPsecOffload -InputObject <CimInstance[]> [-Enabled <Boolean>] [-NoRestart] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-NetAdapterIPsecOffload` cmdlet 用于设置网络适配器的 IPsec offload 属性。当启用 IPsec offload 时，该网络适配器会负责执行每个数据包的加密操作，从而降低处理器的使用率。可以通过使用 `Enable-NetAdapterIPsecOffload` 或 `Disable-NetAdapterIPsecOffload` cmdlet 来切换这一功能的启用状态。

## 示例

### 示例 1：在指定的网络适配器上启用 IPsec 外载功能
```
PS C:\> Set-NetAdapterIPsecOffload -Name "MyAdapter" -Enabled $True
```

此命令可以在名为“MyAdapter”的网络适配器上启用IPsec卸载功能，并重新启动该网络适配器。**Enable-NetAdapterIPsecOffload** cmdlet是执行此操作的推荐命令行工具。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行该cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Enabled
指定 IPsec 转发的状态。该参数的可接受值为：$True 或 $False。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHidden
该参数表示该cmdlet在操作过程中会同时包含可见的网络适配器和隐藏的网络适配器。默认情况下，仅包含可见的网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将用于匹配所有类型的网络适配器（无论是可见的还是隐藏的）。

```yaml
Type: SwitchParameter
Parameter Sets: ByName, ByInstanceID
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。你可以使用该参数，也可以将输入数据通过管道（pipe）传送到这个cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -InterfaceDescription
指定一个网络适配器接口描述数组。对于物理网络适配器而言，这通常是网络适配器的供应商名称后跟部件编号和描述，例如 `Contoso 12345 千兆网络设备`。

```yaml
Type: String[]
Parameter Sets: ByInstanceID
Aliases: ifDesc, InstanceID

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases: ifAlias, InterfaceAlias

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -NoRestart
表示该 cmdlet 在完成操作后不会重新启动网络适配器。许多高级属性要求在新设置生效之前重新启动网络适配器。

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
返回一个表示您当前正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定可以同时建立的、用于运行该cmdlet的操作的最大数量。如果省略此参数或输入`0`，那么Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算出一个最优的速率限制（throttle limit）。该速率限制仅适用于当前正在运行的cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter IPsecOffloadV2SettingData[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapter IPsecOffloadV2SettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Disable-NetAdapterIPsecOffload](./Disable-NetAdapterIPsecOffload.md)

[Enable-NetAdapterIPsecOffload](./Enable-NetAdapterIPsecOffload.md)

[Get-NetAdapterIPsecOffload](./Get-NetAdapterIPsecOffload.md)

