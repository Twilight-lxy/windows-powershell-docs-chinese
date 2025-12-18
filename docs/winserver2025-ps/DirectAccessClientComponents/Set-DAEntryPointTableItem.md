---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DASiteTableEntry.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/set-daentrypointtableitem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DAEntryPointTableItem
---

# Set-DAEntryPointTableItem

## 摘要
修改存储在组策略对象中的 DirectAccess 入口点的配置。

## 语法

### ByPolicyStore（默认值）
```
Set-DAEntryPointTableItem [-EntryPointName <String[]>] -PolicyStore <String> [-ADSite <String>]
 [-EntryPointRange <String[]>] [-TeredoServerIP <String>] [-EntryPointIPAddress <String>] [-GslbIP <String>]
 [-IPHttpsProfile <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByGpoSession
```
Set-DAEntryPointTableItem [-EntryPointName <String[]>] -GPOSession <String> [-ADSite <String>]
 [-EntryPointRange <String[]>] [-TeredoServerIP <String>] [-EntryPointIPAddress <String>] [-GslbIP <String>]
 [-IPHttpsProfile <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-DAEntryPointTableItem -InputObject <CimInstance[]> [-ADSite <String>] [-EntryPointRange <String[]>]
 [-TeredoServerIP <String>] [-EntryPointIPAddress <String>] [-GslbIP <String>] [-IPHttpsProfile <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-DA EntryPointTableItem` cmdlet 用于修改存储在组策略对象（GPO）中的入口点配置。您必须指定包含 DirectAccess 入口点配置的 GPO 的名称。

## 示例

#### 示例 1：修改入口点
```
PS C:\> Set-DAEntryTableItem -EntryPointName "Paris" -GslbIP "131.107.0.1" -PolicyStore "Contoso\GPO1"
```

此cmdlet用于修改名为“Paris”的入口点的GSLB（全球负载均衡）设置。

### 示例 2：使用输入对象修改入口点
```
PS C:\> $x = Set-DAEntryTableItem -EntryPointName "Paris" -PolicyStore "Contoso\GPO1"
PS C:\> $x.GslbIP = 131.107.0.1
PS C:\> $x | Set-DAEntryTableItem
```

此cmdlet通过管道传递一个输入对象来修改名为“Paris”的入口点。

## 参数

### -ADSite
指定与入口点关联的 Active Directory 域服务（AD DS）站点名称。当客户端计算机连接到某个入口点时，该计算机就会与该指定的 AD DS 站点建立关联。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
在运行该cmdlet之前，会提示您进行确认。

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

### -EntryPointIPAddress
指定用于连接的入口点的 IPv6 地址。如果指定的 IP 地址不在 *EntryPointRange* 指定的 IP 地址范围内，该 cmdlet 将会失败。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EntryPointName
指定要修改的入口点的名称。入口点名称通常是该位置的友好名称，例如“Redmond”或“Paris”。

使用双引号 (“”) 指定入口点的名称。

```yaml
Type: String[]
Parameter Sets: ByPolicyStore, ByGpoSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EntryPointRange
指定通过此入口点连接的计算机所使用的 IPv6 地址范围。请使用无类别域间路由（CIDR）表示法来指定该 IPv6 地址范围。

以下是一个 * EntryPointRange* 入口的示例：

`{2001:4898:e0:305d::100:1/128, 2001:4898:e0:305d::100:2/128, 2001:4898:e0:3084::/64}`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GPOSession
指定用于发送配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** 命令集，来汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

```yaml
Type: String
Parameter Sets: ByGpoSession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -GslbIP
指定与新入口点关联的 IP 地址（如果在使用 DirectAccess 时结合了全局服务器负载均衡（GSLB）站点均衡功能）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPHttpsProfile
指定用于连接的 IPHTTPs 配置文件名称。配置文件的名称需要用双引号 (“”) 括起来。如果指定的配置文件在包含相应设置的 GPO 中还不存在，`New-DAEntryPointTableItem` 命令将执行失败。有关 IPHTTPs 配置文件的更多信息，请参阅 `NetworkTransition` 模块中的 `NetIPHTTPsConfiguration` cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

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

### -PassThru
该cmdlet会将交互式窗口中的项目作为输入数据传递给其他cmdlets。默认情况下，这个cmdlet不会生成任何输出结果。不过，如果要将这些项目传递到其他cmdlets中，请先点击鼠标选择所需的项目，然后再点击“确定”按钮。同时支持使用Shift键或Ctrl键进行多选操作。

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

### -PolicyStore
指定该cmdlet将入口点添加到的策略存储库。

要将入口点添加到组策略对象（Group Policy Object）中，请使用以下格式指定 GPO 的名称：“Domain\GPOName”。

要将入口点信息添加到计算机的本地组策略对象（GPO）中，请以“GPO:<计算机名称>”的格式指定该计算机的本地GPO名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

```yaml
Type: String
Parameter Sets: ByPolicyStore
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TeredoServerIP
为新入口点指定Teredo服务器的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的命令（cmdlet）的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM 命令的数量来计算该命令的最佳限制值。此限制仅适用于当前执行的命令，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFT_DASiteTableEntry
此cmdlet返回一个CIM对象，其中包含DA入口点表项。

## 输出

### 无

## 备注

## 相关链接

[Get-DA EntryPointTableItem](./Get-DAEntryPointTableItem.md)

[New-DAEntryPointTableItem](./New-DAEntryPointTableItem.md)

[Remove-DAEntryPointTableItem](./Remove-DAEntryPointTableItem.md)

[ Rename-DA EntryPointTableItem](./Rename-DAEntryPointTableItem.md)

[Reset-DA EntryPointTableItem](./Reset-DAEntryPointTableItem.md)

