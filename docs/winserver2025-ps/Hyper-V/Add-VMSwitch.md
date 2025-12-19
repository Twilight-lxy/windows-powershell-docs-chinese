---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmswitch?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMSwitch
---

# Add-VMSwitch

## 摘要
向以太网资源池中添加虚拟交换机。

## 语法

### NetworkByName（默认值）
```
Add-VMSwitch [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-ResourcePoolName] <String[]> [<CommonParameters>]
```

### NetworkByObject
```
Add-VMSwitch [-VMSwitch] <VMSwitch[]> [-ResourcePoolName] <String[]> [<CommonParameters>]
```

## 描述
`Add-VMSwitch` cmdlet 可以将一个虚拟交换机添加到以太网资源池中。

## 示例

### 示例 1
```
PS C:\> Add-VMSwitch -Name Test -ResourcePoolName "Engineering Department"
```

将虚拟交换机“Test”添加到工程部门的以太网资源池中。

### 示例 2
```
PS C:\> Get-VMSwitch -Name Test | Add-VMSwitch -ResourcePoolName "Engineering Department"
```

将虚拟交换机“Test”添加到工程部门的以太网资源池中。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: NetworkByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个Hyper-V主机的数组。该cmdlet会在您指定的Hyper-V主机上添加虚拟交换机。

```yaml
Type: String[]
Parameter Sets: NetworkByName
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
Parameter Sets: NetworkByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要添加的虚拟交换机的名称。

```yaml
Type: String[]
Parameter Sets: NetworkByName
Aliases: SwitchName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ResourcePoolName
指定要添加虚拟交换机的资源池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitch
指定要添加到以太网资源池中的虚拟交换机。

```yaml
Type: VMSwitch[]
Parameter Sets: NetworkByObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无

默认情况下，此cmdlet不会返回任何输出结果。

### Microsoft.HyperV.PowerShell.VMNetwork

当你使用 **PassThru** 参数时，此 cmdlet 会返回一个 **Microsoft.HyperV.PowerShell.VMNetwork** 对象。

## 备注

## 相关链接

