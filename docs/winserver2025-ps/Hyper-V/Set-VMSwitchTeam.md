---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmswitchteam?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMSwitchTeam
---

# Set-VMSwitchTeam

## 摘要
配置一个虚拟交换机团队。

## 语法

### SwitchName_NetAdapterName（默认值）
```
Set-VMSwitchTeam [-ComputerName <String[]>] [-Name] <String[]> [-NetAdapterName <String[]>]
 [-TeamingMode <VMSwitchTeamingMode>] [-LoadBalancingAlgorithm <VMSwitchLoadBalancingAlgorithm>] [-Passthru]
 [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchName_NetAdapterInterfaceDescription
```
Set-VMSwitchTeam [-ComputerName <String[]>] [-Name] <String[]> [-NetAdapterInterfaceDescription <String[]>]
 [-TeamingMode <VMSwitchTeamingMode>] [-LoadBalancingAlgorithm <VMSwitchLoadBalancingAlgorithm>] [-Passthru]
 [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterInterfaceDescription
```
Set-VMSwitchTeam [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]>
 [-NetAdapterInterfaceDescription <String[]>] [-TeamingMode <VMSwitchTeamingMode>]
 [-LoadBalancingAlgorithm <VMSwitchLoadBalancingAlgorithm>] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterName
```
Set-VMSwitchTeam [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]> [-NetAdapterName <String[]>]
 [-TeamingMode <VMSwitchTeamingMode>] [-LoadBalancingAlgorithm <VMSwitchLoadBalancingAlgorithm>] [-Passthru]
 [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMSwitchTeam` cmdlet 用于配置虚拟交换机团队（virtual switch team）。

## 示例

#### 示例 1：配置交换机团队以实现用户动态负载均衡
```
PS C:\> Set-VMSwitchTeam -Name "SwitchTeam07" -LoadBalancingAlgorithm Dynamic
```

此命令配置名为 SwitchTeam07 的交换机团队使用动态负载均衡算法。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定的域名进行识别。默认值为本地计算机。若要明确指定本地计算机，可使用“localhost”或点（.）。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: PSComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LoadBalancingAlgorithm
指定该交换机组所使用的负载均衡算法。该参数的可接受值为：Dynamic 和 HyperVPort。默认值为 Dynamic。

```yaml
Type: VMSwitchLoadBalancingAlgorithm
Parameter Sets: (All)
Aliases:
Accepted values: HyperVPort, Dynamic

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个虚拟交换机名称数组，该cmdlet将使用这些交换机来进行组队（teaming）配置。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterName, SwitchName_NetAdapterInterfaceDescription
Aliases: SwitchName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterInterfaceDescription
指定一个接口描述数组，用于描述该cmdlet将包含在交换机团队中的虚拟网络适配器。此值会替换现有的成员。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterInterfaceDescription, SwitchObject_NetAdapterInterfaceDescription
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterName
指定一个虚拟网络适配器名称数组，该cmdlet会将这些适配器包含到交换机团队中。此值将替换现有的成员。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterName, SwitchObject_NetAdapterName
Aliases: InterfaceAlias

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此cmdlet会返回它所配置的`Microsoft.HyperV.PowerShell.VMSwitch`对象。

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

### -TeamingMode
指定团队协作模式。目前，唯一可选的模式是 SwitchIndependent。

```yaml
Type: VMSwitchTeamingMode
Parameter Sets: (All)
Aliases:
Accepted values: SwitchIndependent

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitch
指定一组虚拟交换机，该cmdlet将用于配置这些交换机的协作功能。要获取一个**VMSwitch**对象，请使用**Get-VMSwitch** cmdlet。

```yaml
Type: VMSwitch[]
Parameter Sets: SwitchObject_NetAdapterInterfaceDescription, SwitchObject_NetAdapterName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSwitch
如果你指定了 **Passthru** 参数，此 cmdlet 会返回一个 **VMSwitch** 对象。

## 备注

## 相关链接

[Get-VMSwitchTeam](./Get-VMSwitchTeam.md)

[Get-VMSwitch](./Get-VMSwitch.md)

