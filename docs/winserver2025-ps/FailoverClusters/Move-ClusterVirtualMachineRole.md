---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 01/10/2023
online version: https://learn.microsoft.com/powershell/module/failoverclusters/move-clustervirtualmachinerole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Move-ClusterVirtualMachineRole
---

# 移动集群虚拟机角色

## 摘要
将集群虚拟机的所有权转移到另一个节点上。

## 语法

```
Move-ClusterVirtualMachineRole [[-Name] <String>] [[-Node] <String>] [-Cancel]
 [-MigrationType <VmMigrationType>] [-IgnoreLocked] [-VMId <Guid>] [-Wait <Int32>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Move-ClusterVirtualMachineRole` cmdlet 将集群中虚拟机的所有权转移到另一个节点上。

此cmdlet用于实时迁移集群虚拟机。为了快速完成迁移，可以先使用`Get-ClusterResource`和`Set-ClusterParameter`来设置虚拟机资源的**OfflineAction**参数（以保存状态），然后将`Move-ClusterGroup`命令用于执行迁移操作；或者直接在调用`Move-ClusterGroup`之前将`OfflineAction`参数的值设置为1。

注意：如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）身份验证功能，此 cmdlet 无法远程运行。

## 示例

### 示例 1

```powershell
Move-ClusterVirtualMachineRole -Name "Virtual Machine1" -Node node2
```

这个示例将名为“Virtual Machine1”的集群虚拟机实时迁移到名为`node2`的节点上。在迁移操作完成之前，Windows PowerShell提示符不会返回任何信息。

### 示例 2

```powershell
Get-ClusterGroup -Name "Virtual Machine1" | Move-ClusterVirtualMachineRole -Node node2 -Wait 0
```

这个示例将名为 `Virtual Machine1` 的集群化虚拟机实时迁移到了名为 `node2` 的节点上。一旦操作开始，Windows PowerShell 提示符就会立即返回。

### 示例 3

```powershell
Move-ClusterVirtualMachineRole -Name "Virtual Machine1" -Cancel
```

这个示例会取消名为`Virtual Machine1`的集群虚拟机正在进行的实时迁移操作。

### 示例 4

```powershell
$vmGroups = Get-ClusterNode -Name node1 |
    Get-ClusterGroup |
    Where-Object -FilterScript {
        Get-ClusterResource -InputObject $_ |
            Where-Object ResourceType -Like "Virtual Machine"
    }
ForEach-Object -InputObject $vmGroups -Process { $_ | Move-ClusterVirtualMachineRole -Node node2 }
```

这个示例查询特定的集群节点（`node1`），以找到该节点当前拥有的所有组。接着，该示例进一步筛选出那些资源类型为虚拟机集群资源的组，并将这些筛选出的组存储在变量 `$vmGroups` 中。对于变量 `$vmGroups` 中的每个集群组，命令会将所有属于该组的虚拟机实时迁移到名为 `node2` 的节点上。每台虚拟机的迁移完成后，才会开始下一台的迁移过程。

## 参数

### -Cancel

指定取消正在进行的虚拟机实时迁移操作。

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

### -Cluster

指定用于运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -IgnoreLocked

指定在运行该 cmdlet 时忽略已锁定的组。

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

### -InputObject

指定要迁移的集群化虚拟机。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -MigrationType

指定要对虚拟机执行的迁移类型。可选方案如下：

- `Live`: Transparently migrates the virtual machine without a dropped network connection or
  perceived downtime.

- `Quick`: Rapidly migrates a running virtual machine with minimal downtime.

- `Shutdown`: Performs an orderly shutdown of the operating system (waiting for all processes to
  close) on the virtual machine, and then migrates the virtual machine.

- `ShutdownForce`: Shuts down the operating system on the virtual machine without waiting for slower
  processes to finish, and then migrates the virtual machine.

- `TurnOff`: Turns off the virtual machine without shutting down the operating system first, then
  migrates the virtual machine. This is the same as turning off the power, which means that data
  loss may occur.

```yaml
Type: VmMigrationType
Parameter Sets: (All)
Aliases:
Accepted values: TurnOff, Quick, Shutdown, ShutdownForce, Live

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name

指定要移动的集群化虚拟机的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Node

指定要移动虚拟机的集群节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMId

指定虚拟机标识符（ID）。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Wait

该参数用于指定等待cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到操作完成；如果指定了`-Wait 0`，则cmdlet会立即开始执行并立即返回结果，而不会进行任何等待。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellClusterGroup

## 输出

### MicrosoftFailoverClusters.PowerShellClusterGroup

## 备注

## 相关链接

[添加集群虚拟机角色](./Add-ClusterVirtualMachineRole.md)

[更新集群虚拟机配置](./Update-ClusterVirtualMachineConfiguration.md)
