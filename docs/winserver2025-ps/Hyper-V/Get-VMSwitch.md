---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmswitch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMSwitch
---

# Get-VMSwitch

## 摘要
获取一台或多台Hyper-V主机上的虚拟交换机信息。

## 语法

### 名称（默认值）
```
Get-VMSwitch [[-Name] <String>] [[-ResourcePoolName] <String[]>] [-SwitchType <VMSwitchType[]>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### ID
```
Get-VMSwitch [[-Id] <Guid[]>] [[-ResourcePoolName] <String[]>] [-SwitchType <VMSwitchType[]>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`Get-VMSwitch` cmdlet 用于从 Hyper-V 主机中获取虚拟交换机。如果您不指定任何参数，该 cmdlet 将返回本地 Hyper-V 主机上所有的虚拟交换机。

## 示例

### 示例 1
```
PS C:\> Get-VMSwitch
```

从本地 Hyper-V 主机中获取所有虚拟交换机。

### 示例 2
```
PS C:\> Get-VMSwitch -SwitchType External
```

获取所有连接到外部网络的虚拟交换机。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet将在本地计算机的当前会话中运行。

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
指定一个或多个用于获取虚拟交换机的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机标识。默认值是本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

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

### -Id
指定要检索的虚拟交换机的唯一标识符。

```yaml
Type: Guid[]
Parameter Sets: Id
Aliases: SwitchId

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定要检索的虚拟交换机的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases: SwitchName

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定用于获取虚拟交换机的资源池。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SwitchType
指定要检索的虚拟交换机的类型。允许的值有 **External**（外部）、**Internal**（内部）和 **Private**（私有）。

```yaml
Type: VMSwitchType[]
Parameter Sets: (All)
Aliases:
Accepted values: Private, Internal, External

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShell.VMSwitch

## 备注

## 相关链接

