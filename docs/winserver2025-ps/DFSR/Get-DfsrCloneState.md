---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/get-dfsrclonestate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DfsrCloneState
---

# Get-DfsrCloneState

## 摘要
获取数据库克隆操作的状态。

## 语法

```
Get-DfsrCloneState [<CommonParameters>]
```

## 描述
`Get-DfsrCloneState` 这个 cmdlet 可以获取本地计算机上正在进行的卷克隆操作的状态。该 cmdlet 会返回分布式文件系统（DFS）复制数据库或卷的配置 XML 文件设置导出或导入过程的当前状态。

此cmdlet没有任何参数，仅返回状态信息。您必须在该执行导出或导入操作的DFS复制计算机上运行此cmdlet。在一台服务器上一次只能进行一个导入或导出操作。

DFS复制服务可以返回以下克隆状态：

- Ready. The DFS Replication service is ready to perform cloning. This is the status both before cloning starts and after cloning completes.
- Started DB Export. The DFS Replication service has begun the export process and is validating prerequisites.
- Started DB Import. The DFS Replication service has begun the import process and is validating prerequisites.
- Processing DB Export. The DFS Replication service is exporting the database.
- Processing DB Import. The DFS Replication service is importing the database.
- Resetting. The DFS Replication service is cancelling and rolling back the import or export.
- Shut down. The DFS Replication database is shut down due to a requested backup or restore operation.
- Shutting down. The DFS Replication database is shutting down because of a requested backup or restore operation, or because of a requested service shut down.

## 示例

### 示例 1：获取分布式文件系统（DFS）复制克隆的状态
```
PS C:\> Get-DfsrCloneState
Ready
```

这个命令用于获取DFS复制克隆的状态。在这种情况下，服务器当前并未处于克隆状态；克隆操作既没有开始，也没有完成。

### 示例 2：在克隆操作过程中获取状态信息
```
The first command exports a cloned DFS Replication database and volume configuration settings from C:\DfsRClone.
PS C:\> Export-DfsrClone -Volume "C:" -Path "C:\DfsRClone" -Force

The second command returns the state that indicates that the DFSR service has begun the export process and is validating prerequisites.
PS C:\> Get-DfsrCloneState
Started DB Export

The third command returns the state that indicates that the DFS Replication service is exporting the database.
PS C:\> Get-DfsrCloneState
Processing DB Export

The fourth command returns the state that indicates that the cloning is complete and the DFS Replication service is ready to perform cloning.
PS C:\> Get-DfsrCloneState
Ready
```

这个示例用于导出DFS复制数据库的副本，并获取正在进行中的克隆操作的状态。第一个命令在一个Windows PowerShell控制台中执行，其余命令则在另一个Windows PowerShell控制台中执行。这样做是必要的，因为`Export-DfsrClone` cmdlet只有在DFS复制服务完成导出操作或用户按下Ctrl + C退出该cmdlet时才会返回结果。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### DfsrCloneState

## 备注

## 相关链接

[Import-DfsrClone](./Import-DfsrClone.md)

[Export-DfsrClone](./Export-DfsrClone.md)

[Reset-DfsrCloneState](./Reset-DfsrCloneState.md)

